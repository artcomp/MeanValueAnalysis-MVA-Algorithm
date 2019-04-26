import matplotlib.pyplot as plt


def print_header():
	
	print ("iter\t",

			"X\t", 
			
			"N_d,a\t", 
			"N_d,b\t", 
			"N_cpu\t", 

			"R_d,a\t", 
			"R_d,b\t", 
			"R_cpu\t", 

			"U_d,a\t", 
			"U_d,b\t", 
			"U_cpu\t", 

			"R\t")
	
	print ("-----------------------------------------------------------------------------------------------")
	
def printInfoTable(X0,Ni,Ri,Ui,R,n):
	print (	n ,"\t",
				round(X0,3),"\t", 


				round(Ni[0],3),"\t", 
				round(Ni[1],3),"\t", 
				round(Ni[2],2),"\t",

				round(Ri[0],3),"\t",
				round(Ri[1],3),"\t",
				round(Ri[2],3),"\t",

				round(Ui[0],3),"\t",
				round(Ui[1],3),"\t",
				round(Ui[2],3),"\t",

				round(R,3))


def plotDataTempoDeResposta(D,Z,Dmax,y_pessimista_n_menor_po,y_pessimista_n_maior_po, n, _list_X0, _list_R):
	x_axis = [x for x in range(0,n+1)]
	ones_list = list(map(lambda x: 1, x_axis))
	
	#limites otimistas
	y_otimista_n_menor_po = list(map(lambda x: x*D,ones_list))
	y_otimista_n_maior_po = list(map(lambda x: (x*(Dmax) - 2),x_axis))
	
	#plota graficos
	
	#otimistas
	plt.plot(x_axis, y_otimista_n_menor_po,'-.r',label='limite pessimista para N < N*')
	plt.plot(x_axis, y_otimista_n_maior_po, '-.b',label='limite pessimista para N > N*')

	#pessimistas
	plt.plot(x_axis, y_pessimista_n_menor_po,'--g',label='limite otimista para N < N*')
	plt.plot(x_axis, y_pessimista_n_maior_po, '--m',label='limite otimista para N > N*')

	#mva
	plt.plot(x_axis, _list_R, '-k',label='MVA')

	plt.title('Limites Assintóticos Tempo de Resposta')
	plt.xlabel('N', color='#1C2833')
	plt.ylabel('R(N)', color='#1C2833')
	plt.legend(loc='best')
	plt.show()

def plotDataThroughput(D,Z,Dmax,y_pessimista_n_menor_po,y_pessimista_n_maior_po, n, _list_X0, _list_R):

	x_axis = [x for x in range(0,n+1)]
	ones_list = list(map(lambda x: 1, x_axis))

	#limites otimistas

	y_otimista_n_menor_po = list(map(lambda x: x*(1 / (D + Z)),x_axis))
	#ajuste do grafico
	y_otimista_n_menor_po = cutLimitThroughput(y_otimista_n_menor_po, Dmax)

	y_otimista_n_maior_po = list(map(lambda x: x*(1 / (Dmax) ),ones_list))
	y_otimista_n_maior_po = cutLimitThroughput(y_otimista_n_maior_po, Dmax)
	
	#plota graficos
	
	#otimistas
	plt.plot(x_axis, y_otimista_n_menor_po,'-.r',label='limite otimista para N < N*')
	plt.plot(x_axis, y_otimista_n_maior_po, '-.b',label='limite otimista para N > N*')

	#pessimistas
	plt.plot(x_axis, y_pessimista_n_menor_po,'--g',label='limite pessimista para N < N*')
	plt.plot(x_axis, y_pessimista_n_maior_po, '--m',label='limite pessimista para N > N*')

	#mva
	plt.plot(x_axis, _list_X0, '-k',label='MVA')

	plt.title('Limites Assintóticos Throughput')
	plt.xlabel('N', color='#1C2833')
	plt.ylabel('X(N)', color='#1C2833')
	plt.legend(loc='best')
	plt.show()

def cutLimitThroughput(lista, Dmax):
	return list(map(lambda x: ((1/Dmax)*1.5) if x > ((1/Dmax)*1.5) else x, lista))
