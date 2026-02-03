from abc import ABC, abstractmethod

class BaseRegulator(ABC):
    """
        Базовый класс
        dt - 1 секунда — как часто регулятор "думает"
    """
    def __init__(self, dt=1.0):
        self.dt = dt

    @abstractmethod
    def update(self, setpoint, current_temp):
        pass

class IRegulator(BaseRegulator):
    def __init__(self, ki=0.05, dt=1.0):
        super().__init__(dt)
        self.ki = ki
        self.integral = 0.0
    
    def update(self, setpoint, current_temp):
        error = setpoint - current_temp
        self.integral += error * self.dt
        return self.ki * self.integral 

class PIRegulator(BaseRegulator):
    def __init__(self, kp=3.5, ki=0.04, dt=1.0):
        super().__init__(dt)
        self.kp = kp
        self.ki = ki
        self.integral = 0.0
    
    def update(self, setpoint, current_temp):
        error = setpoint - current_temp
        self.integral += error * self.dt
        return self.kp * error + self.ki * self.integral  

class PIDRegulator(BaseRegulator):
    def __init__(self, kp=15.0, ki=0.08, kd=8.0, dt=1.0):  
        super().__init__(dt)
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.integral = 0.0
        self.prev_error = 0.0
    
    def update(self, setpoint, current_temp):
        error = setpoint - current_temp
        self.integral += error * self.dt
        derivative = (error - self.prev_error) / self.dt
        self.prev_error = error
        return (self.kp * error + 
                self.ki * self.integral + 
                self.kd * derivative)
