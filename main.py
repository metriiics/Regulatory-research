import numpy as np
import matplotlib.pyplot as plt
from temp import ThermalModel
from Regulator import (IRegulator, PIRegulator, PIDRegulator)

def simulate(regulator, setpoint=80.0, total_time=800, dt=1.0):
    model = ThermalModel(tau=50)  
    time = np.arange(0, total_time, dt)
    temps = np.zeros(len(time))
    temps[0] = model.current_temp
    
    for i in range(1, len(time)):
        control = regulator.update(setpoint, temps[i-1])
        temps[i] = model.step(control, dt)
    
    return time, temps

def plot_all(regulators, names):
    # 3 отдельных графика
    for regulator, name in zip(regulators, names):
        time, temps = simulate(regulator)
        plt.figure(figsize=(12, 6))
        plt.plot(time, temps, 'b-', linewidth=3, label='Температура')
        plt.plot(time, [80]*len(time), 'r--', linewidth=3, label='Уставка')
        plt.title(f'{name}-регулятор')
        plt.xlabel('Время, с')
        plt.ylabel('Температура, °C')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.show()
    
    # Сравнение всех
    fig, ax = plt.subplots(figsize=(15, 8))
    colors = ['blue', 'red', 'orange', 'purple']
    
    for i, (regulator, name) in enumerate(zip(regulators, names)):
        time, temps = simulate(regulator)
        ax.plot(time, temps, label=name, linewidth=4, color=colors[i])
    
    ax.plot(time, [80]*len(time), 'k--', linewidth=4, label='Уставка')
    ax.set_title('Регуляторов')
    ax.set_xlabel('Время, с')
    ax.set_ylabel('Температура, °C')
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.show()

def main():
    regulators = [
        IRegulator(ki=0.05),
        PIRegulator(kp=0.5, ki=0.07),
        PIDRegulator(kp=0.5, ki=0.05, kd=0.05) 
    ]
    names = ['И', 'ПИ', 'ПИД']
    
    plot_all(regulators, names)


if __name__ == "__main__":
    main()
