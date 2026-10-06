#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Color
from pybricks.robotics import DriveBase

# 1. Inicialização do Bloco e Dispositivos
ev3 = EV3Brick()

# Ajuste as portas dos motores conforme a sua montagem
left_motor = Motor(Port.A)
right_motor = Motor(Port.B)

# Ajuste as portas dos sensores de cor
left_sensor = ColorSensor(Port.S1)
right_sensor = ColorSensor(Port.S2)

# Configuração da base motora (DriveBase)
# Diâmetro da roda em mm e distância entre as rodas (track) em mm
robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=114)

# Definindo velocidades de navegação
SPEED = 100        # Velocidade em frente (mm/s)
TURN_SPEED = 60    # Velocidade de rotação nas curvas (deg/s)

# Sinal sonoro indicando que o programa iniciou
ev3.speaker.beep()

# 2. Loop Principal de Seguidor de Linha por Cores
while True:
    # Leitura das cores identificadas pelos dois sensores
    left_color = left_sensor.color()
    right_color = right_sensor.color()

    # Se o sensor esquerdo viu a linha preta -> Corrigir virando para a esquerda
    if left_color == Color.BLACK and right_color != Color.BLACK:
        robot.drive(0, -TURN_SPEED)

    # Se o sensor direito viu a linha preta -> Corrigir virando para a direita
    elif right_color == Color.BLACK and left_color != Color.BLACK:
        robot.drive(0, TURN_SPEED)

    # Se ambos os sensores estão no branco -> Seguir em frente
    elif left_color == Color.WHITE and right_color == Color.WHITE:
        robot.drive(SPEED, 0)

    # Se ambos os sensores detectarem preto (Cruzamento) -> Seguir em frente
    elif left_color == Color.BLACK and right_color == Color.BLACK:
        robot.drive(SPEED, 0)

    # Caso estejam em outra superfície/cor genérica
    else:
        robot.drive(SPEED, 0)


