
def ESCal(L,W,FB,K,CH,PH):
    ES=[]
    for i in range(len(L)):
        ans=L[i] * W[i] * (1 + FB[i]) * (1/K) * (CH[i] - PH[i])
        ES.append(ans)
    print("ES:", ES)
    return ES

def DRCal(L,W,FB,K,CF,M):
    DR=[]
    for i in range(len(L)):
        ans=L[i] * W[i] * (1 + FB[i]) * (1/K) * (1-CF[i]) * M
        DR.append(ans)
    print("DR:", DR)
    return DR

def CSCal(ES,DR,EEC,EDC):
    CS=0
    for i in range(len(ES)):
        CS+= ES[i]*EEC + DR[i]*EDC
    return CS

def OSARCal(L:list[int],W:list[float],FB:list[float],K:int,CH:list[float],PH:
            list[float],M:int,EEC:float,EDC:float):
    if len(L) != len(W) or len(L) != len(FB) or len(L) != len(CH) or len(L) != len(PH):
        raise ValueError("Length of all input lists must be the same")
    ES = ESCal(L,W,FB,K,CH,PH)
    CF = []
    for i in range(len(CH)):
        CF.append( PH[i]/CH[i] )
    DR = DRCal(L,W,FB,K,CF,M)
    CS = CSCal(ES,DR,EEC,EDC)
    print("CS:", CS)
    return CS
    
#EXAMPLE
L=[]
W=[]
FB=[]
K=1000
CH=[]
PH=[]
#CF=[]
#for i in range(len(CH)):
#    CF.append( PH[i]/CH[i] )
M=12
#ES= ESCal(L,W,FB,K,CH,PH)
#DR= DRCal(L,W,FB,K,CF,M)
CS=OSARCal(L,W,FB,K,CH,PH,M,EEC=,EDC=)
