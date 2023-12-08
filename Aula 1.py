# QUESTIONÁRIO SIMPLES DE PERGUNTAS E RESPOSTAS!!


print('Olá, vamos começar ? irei iniciar o questionário com algumas perguntas básicas sobre você. :D')

nome = input('qual o seu nome ?')
sobrenome = input('Agora me fale seu sobrenome:')
aperlido = input('Como seus amigos te chamam?')
idade = input('qual a sua idade ?')
e_mail = input('Digite o seu E-mail ?')
desejo = input('Qual o seu maior desejo?')

texto0 = f'você se chama {nome} {sobrenome} e tem {idade} anos e seu melhor E-mail é {e_mail}, seu maior desejo é {desejo}, {nome} vamos continuar!'
print(texto0)

texto1 = f'já que você tem {idade} anos, então você nasceu no ano de '
idade = int(2023) - int(idade)
print(f' {texto1}{idade}')

print(f'obrigado por me falar um pouco sobre você, até maiS {aperlido} :D.')
