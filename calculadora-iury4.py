print("Escolha uma operação")
print('m = multiplicação')
print('d = divisão')
print('a = adição')
print('s = subtração')

escolha = input('Digite uma das operações desejadas entre m,d,a,s: ')
digite_um_numero = float(input("Digite um Número: "))
digite_mais_um = float(input("Digite um Número: "))
if escolha == 'm':
  result=digite_um_numero*digite_mais_um
  print(f'Resultado:',{result})
elif escolha == 'd':
  if digite_mais_um != 0:
    result=digite_um_numero/digite_mais_um
    print('Resultado',{result})
  else:
     print('Impossível dividir por zero')
elif escolha == 'a':
      result=digite_um_numero+digite_mais_um
      print(f'Resultado',{result})
elif escolha == 's':
  result=digite_um_numero-digite_mais_um
  print(f'Resultado',{result})
else:
  print('Por favor escolha uma letra entre m,d,a,s')
