from view import *

def MVA_exato(N, Z, K, Si, Vi, e):
	Ni = []
	Ri = []
	X0 = 0.0
	Di = []
	D = 0
	Dmax = -1
	_list_X0 = []
	_list_R = []

	y_pessimista_n_menor_po_throughput = []
	y_pessimista_n_maior_po_throughput = []
	y_pessimista_n_menor_po_tempo_de_resposta = []
	y_pessimista_n_maior_po_tempo_de_resposta = []

	Di = [(a*b) for a, b in zip(Si, Vi)]
	D = sum(Di)
	Dmax = max(Di)

	print_header()

	for i in range(K):
		Ni.append(0.0)
		Ri.append(0.0)
	
	n=0
	for n in range(N):
		for i in range(K):
			Ri[i] = Si[i] * (1 + Ni[i])

		R = sum([a*b for a, b in zip(Ri, Vi)])
		_list_R.append(R)

		X0 = (n/(R+Z))
		_list_X0.append(X0)


		Ui = [((a*b)*X0) for a, b in zip(Si, Vi)]

		for i in range(K):
			Ni[i] = X0*Vi[i]*Ri[i]
		  
		printInfoTable(X0,Ni,Ri,Ui,R,n)

		#limites pessimistas throughput
		y_pessimista_n_menor_po_throughput.append(n / (n*D + Z))
		y_pessimista_n_maior_po_throughput.append( min( ((n / (D + Z))) , (1/Dmax) ) )

		#limites pessimistas tempo de resposta
		y_pessimista_n_menor_po_tempo_de_resposta.append(max(D,(n*Dmax-Z)))
		y_pessimista_n_maior_po_tempo_de_resposta.append(n*D)

	while True:
		tput_or_tresp = input('\n\nPlotar gráficos ? (s) (n) : ')
		if tput_or_tresp.lower() == 's':

			while True:
				opt = int(input('\n\t1 - Throughput\n\t2 - Tempo de Resposta\n\t3 - Sair\n\n\t\tEscolha : '))
				if opt == 1:
					plotDataThroughput(D,Z,Dmax,y_pessimista_n_menor_po_throughput,y_pessimista_n_maior_po_throughput, n, _list_X0, _list_R)
				elif opt == 2:
					plotDataTempoDeResposta(D,Z,Dmax,y_pessimista_n_menor_po_tempo_de_resposta,y_pessimista_n_maior_po_tempo_de_resposta, n, _list_X0, _list_R)
				else:
					break
		else:
			break



def MVA_aproximado(N, Z, K, Si, Vi, e):
	
	Nii = []
	Ni = []
	Ri = []
	X0 = 0.0
	Di = []
	D = 0
	Dmax = -1
	_list_X0 = []
	_list_R = []

	y_pessimista_n_menor_po_throughput = []
	y_pessimista_n_maior_po_throughput = []
	y_pessimista_n_menor_po_tempo_de_resposta = []
	y_pessimista_n_maior_po_tempo_de_resposta = []

	Di = [(a*b) for a, b in zip(Si, Vi)]
	D = sum(Di)
	Dmax = max(Di)

	print_header()

	
	print_header() 

	for i in range(K):
		Ni.append(float(N/K))
		Ri.append(0.0)
		Nii.append(float(N/K))
	n = 0
	while True:
		for i in range(K):
			Ri[i] = Si[i] * (1 + (((N-1)/N) * Ni[i]))

		R = sum([a*b for a,b in zip(Ri, Vi)])
		_list_R.append(R)

		X0 = float(N/(R+Z))
		_list_X0.append(X0)

		Ui = [((a*b)*X0) for a,b in zip(Si, Vi)]

		for i in range(K):
			 Nii[i] = Ni[i]
		
		for i in range(K):
			Ni[i] = X0*Vi[i]*Ri[i]

		MAXi=max([abs(a-b) for a, b in zip(Ni, Nii)])
		
		printInfoTable(X0,Ni,Ri,Ui,R,n)

		#limites pessimistas throughput
		y_pessimista_n_menor_po_throughput.append(n / (n*D + Z))
		y_pessimista_n_maior_po_throughput.append( min( ((n / (D + Z))) , (1/Dmax) ) )

		#limites pessimistas tempo de resposta
		y_pessimista_n_menor_po_tempo_de_resposta.append(max(D,(n*Dmax-Z)))
		y_pessimista_n_maior_po_tempo_de_resposta.append(n*D)


		if MAXi <= e:
			break
		n = n+1

	while True:
		tput_or_tresp = input('\n\nPlotar gráficos ? (s) (n) : ')
		if tput_or_tresp.lower() == 's':

			while True:
				opt = int(input('\n\t1 - Throughput\n\t2 - Tempo de Resposta\n\t3 - Sair\n\n\t\tEscolha : '))
				if opt == 1:
					plotDataThroughput(D,Z,Dmax,y_pessimista_n_menor_po_throughput,y_pessimista_n_maior_po_throughput, n, _list_X0, _list_R)
				elif opt == 2:
					plotDataTempoDeResposta(D,Z,Dmax,y_pessimista_n_menor_po_tempo_de_resposta,y_pessimista_n_maior_po_tempo_de_resposta, n, _list_X0, _list_R)
				else:
					break
		else:
			break


def main():

	# Da, Db, CPU
	N = 30+1
	Z = 5
	K = 3
	Si = [0.03,0.025,0.04]
	Vi = [20,4,25]
	e = 0.01

	opcao = int(input("\n\n\t\tAlgoritmos MVA\n\n\nEscolha um método : \n\n\tAproximado -> 1\n\tExato -> 0\n\n\t\tEscolha : "))
	MVA_aproximado(N, Z, K, Si, Vi, e) if opcao else MVA_exato(N, Z, K, Si, Vi, e)
	
if __name__ == '__main__':
	main()
