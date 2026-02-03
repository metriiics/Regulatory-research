import numpy as np

class ThermalModel:
    """
    Модель термостата
    
    tau - const, определает, насколько инертна система, чем больше
    тем медленнее температура реагирует на изменения

    current_temp - текущая температура
    """
    def __init__(self, tau=50.0, initial_temp=20.0):
        self.tau = tau 
        self.current_temp = initial_temp
        
    def step(self, control_input, dt=1.0):
        """
        Один шаг симуляции
        
        control_input - входной сигнал управления от регулятора (u(t))

        current_temp - возвращает новую температуру после шага
        """
        dT = (control_input * 0.8 - self.current_temp) * dt / self.tau
        self.current_temp += dT
        return self.current_temp
