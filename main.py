import pandas
import os



def gerar_relatorio(df):
    total_vendas = df["valor"].sum()
    pedidos_por_status = df["status"].value_counts()

    relatorio = {
        "total_vendas": total_vendas,
        "pedidos_por_status": pedidos_por_status.to_dict()
    }

    return relatorio




# Carregando dados
df = pandas.read_csv("pedidos.csv")

# Atualizando status
df.loc[df["status"] == "Pendente", "status"] = "Processando"

# Gerando relatório
relatorio = gerar_relatorio(df)

# Resultados
os.system("cls")
print("------------ Relatório ------------")
print(f"Total de vendas:      R${relatorio['total_vendas']}")
print(f"Pedidos em processo:  {relatorio["pedidos_por_status"]["Processando"]}")
print(f"Pedidos enviados:     {relatorio["pedidos_por_status"]["Enviado"]}")
print("\n")

# Salvar atualização
#df.to_csv("dados/pedidos_atualizados.csv", index=False)