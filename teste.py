import pyMono as Mono

data = Mono.load('40.csv', p0=1, nist_csv=True)

#

#data2 = Mono.Isotherm([2.1,0.7], 8)

resultado = Mono.estimate(data.p, data.q, 'sips')
param=[[0.01, 1], [1, 100], [1, 2]]

resultado.plot(export=True, extension='svg')



