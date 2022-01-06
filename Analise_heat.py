import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import win32com.client as win32

#montado análise
abrir = pd.read_excel('G:\Meu Drive\Registros\Geral\PycharmProjects\Pandass\Heatmap01\int.xlsx')
df = abrir.groupby("Dia Semana").sum().sort_values(by=['Quantidade Chats'],ascending=False)
sns.heatmap(df,cmap="RdBu")
plt.title("Atendimento ")
plt.savefig('Atendimento')
plt.show()

arq = df.to_csv('Dados')

# enviando email

#criando execução do outlook
outlook = win32.Dispatch('outlook.application')
#criar um email "gate" para envio
email = outlook.CreateItem(0)
# configurar o email para envio
email.To = "alex.ssxargemi@gmail.com"
email.subject = "Atendimento"
email.HTMLBody = f"""
    <p> Olá,tudo bem? </p>

    <p> Segue a listagem do resultado de nosso time, na ultima semana em quantidades de chat! </p>
    <p> O numero foi agrupado pelo dia da semana, portanto, o gráfico de calor demonstra em graus qual foi o dia com mais e menos atendimento feito"
    <p> Segue arquivo base em excel e o agrupado em csv, junto com a imagem do gráfico</p>

    <b> <p> Abs </p></b>

    </p>

    """
print("")
anexo = "G:\Meu Drive\Registros\Geral\PycharmProjects\Pandass\Heatmap01\Dados.csv"
anexo2 = "G:\Meu Drive\Registros\Geral\PycharmProjects\Pandass\Heatmap01\Atendimento.png"
anexo3 = "G:\Meu Drive\Registros\Geral\PycharmProjects\Pandass\Heatmap01\int.xlsx"

email.Attachments.Add(anexo)
email.Attachments.Add(anexo2)
email.Attachments.Add(anexo3)
email.Send()

print("Enviado")
