#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Color
from pybricks.robotics import DriveBase

# 1. Inicialização do Bloco e Dispositivos
ev3 = EV3Brick()

# Ajuste as portas dos motores conforme a sua montagem
motorEsquerdo = Motor(Port.A)
motoDireito = Motor(Port.B)

# Ajuste as portas dos sensores de cor
sensor_esquerdo = ColorSensor(Port.S1)
sensor_direito = ColorSensor(Port.S2)

# Configuração da base motora (DriveBase)
robot = DriveBase(motorEsquerdo, motorDireito)

# Definindo velocidades de navegação
VELOCIDADE = 100        # Velocidade em frente (mm/s)
VELOCIDADE_CURVA = 60    # Velocidade de rotação nas curvas (deg/s)

# Sinal sonoro indicando que o programa iniciou
ev3.speaker.beep()

# 2. Loop Principal de Seguidor de Linha por Cores
while True:
    # Leitura das cores identificadas pelos dois sensores
    Cor_esquerdo = sensor_esquerdo.color()
    Cor_direito = right_direito.color()

    # Se o sensor esquerdo viu a linha preta -> Corrigir virando para a esquerda
    if sCor_esquerdo == Color.BLACK and Cor_direito != Color.BLACK:
        robot.drive(0, -VELOCIDADE_CURVA)

    # Se o sensor direito viu a linha preta -> Corrigir virando para a direita
    elif Cor_direito == Color.BLACK and Cor_esquerdo != Color.BLACK:
        robot.drive(0, VELOCIDADE_CURVA)

    # Se ambos os sensores estão no branco -> Seguir em frente
    elif Cor_esquerdo == Color.WHITE and Cor_direito == Color.WHITE:
        robot.drive(VELOCIDADE, 0)

    # Se ambos os sensores detectarem preto (Cruzamento) -> Seguir em frente
    elif Cor_esquerdo == Color.BLACK and Cor_direito == Color.BLACK:
        robot.drive(VELOCIDADE, 0)

    # Caso estejam em outra superfície/cor genérica
    else:
        robot.drive(VELOCIDADE, 0)


