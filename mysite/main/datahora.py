from datetime import date, datetime

def Data():
    data_atual = date.today()
    data_em_texto = data_atual.strftime('%d/%m/%Y')

    return data_em_texto

def Tempo():
    hora_atual = datetime.now()
    hora_em_texto = hora_atual.strftime('%H:%M:%S')

    return hora_em_texto