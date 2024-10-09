velocidade = 62 #velocidade do carro    
local_carro = 90 #km que o carro esta na estrada

RADAR_1 = 60 #velocidade maxima do radar   
LOCAL_1 = 100 #local onde o radar 1 esta
RADAR_RANGE = 1 #a distancia onde o radar pega

velocidade_carro_passou_radar_1 = velocidade > RADAR_1 
carro_multado_radar_1 = local_carro >= (local_carro - RADAR_RANGE) and \
        local_carro <=  (local_carro + RADAR_RANGE)

if velocidade_carro_passou_radar_1 :
    print('A velocidade do carro passou do permitido')

if  carro_multado_radar_1 and velocidade_carro_passou_radar_1 :
    print('Carro multado em radar 1')
else :
    ...
    print('Carro esta na velocidade permitida')



