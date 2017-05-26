import numpy as np
import matplotlib.pyplot as plt

#Se importan los datos y se guardan en arreglos.
datos=np.genfromtxt('CircuitoRC.txt')

t_obs=datos[:,0]
q_obs=datos[:,1]

#Se define la funcion de verosimilitud. Usamos un sigma de 100.
def likelihood(q_obs, q_modelo):
    chi_squared = (1.0/100.0)*np.sum((q_obs-q_modelo)**2)
    return np.exp(-chi_squared)

#Se define la funcion modelo, de acuerdo con la ecuacion (1) de la tarea.
def modelo(t_obs, r, c):
    return 10.0*c*(1-np.exp(-t_obs/(r*c)))

#Se inicializan los arreglos donde se guardaran los datos de las caminatas.
r_walk = np.empty((0))
c_walk = np.empty((0))
l_walk = np.empty((0))

#Se define un guess inicial. R=10 y C=10. Se incluye este guess en los arreglos de las caminatas.
r_walk = np.append(r_walk, 10.0)
c_walk = np.append(c_walk, 10.0)
#Calcula el likelihood inicial
q_init = modelo(t_obs, r_walk[0], c_walk[0])
l_walk = np.append(l_walk, likelihood(q_obs, q_init))

#Haremos 20.000 iteraciones.
iteraciones = 20000
for i in range(iteraciones):
    #El nuevo dato
    r_prime = np.random.normal(r_walk[i], 0.1) 
    c_prime = np.random.normal(c_walk[i], 0.1)

    q_init = modelo(t_obs, r_walk[i], c_walk[i])
    q_prime = modelo(t_obs, r_prime, c_prime)
    
    l_prime = likelihood(q_obs, q_prime)
    l_init = likelihood(q_obs, q_init)
    #Se define el alpha
    alpha = l_prime/l_init
    #Si es mayor a 1 se incluye el dato en la caminata.
    if(alpha>=1.0):
        r_walk  = np.append(r_walk,r_prime)
        c_walk  = np.append(c_walk,c_prime)
        l_walk = np.append(l_walk, l_prime)
    #Sino, solo si alpha es mayor a beta se incluye. Beta es un numero aleatorio.
    else:
        beta = np.random.random()
        if(beta<=alpha):
            r_walk = np.append(r_walk,r_prime)
            c_walk = np.append(c_walk,c_prime)
            l_walk = np.append(l_walk, l_prime)
        else:
            r_walk = np.append(r_walk,r_walk[i])
            c_walk = np.append(c_walk,c_walk[i])
            l_walk = np.append(l_walk, l_init)

#Se encuentran los datos con mayor likelihood. Ese es el mejor fit.
max_id = np.argmax(l_walk)
best_r = r_walk[max_id]
best_c = c_walk[max_id]
best_q = modelo(t_obs, best_r, best_c)
q_max=best_c*10.0

#Se grafican los resultados.
plt.figure()
plt.subplot(321)
plt.scatter(t_obs, q_obs, s = 8, label='observados')
plt.plot(t_obs, best_q, color='red', label='best fit')
plt.legend(loc=0, fontsize=8)
plt.title('$R=%f$, $C=%f$, $Q=%f$' %(best_r, best_c, q_max), fontsize=9)
plt.subplot(322)
plt.scatter(r_walk, c_walk, label='R_walk vs C_walk', color='red', s=8)
plt.legend(loc=0, fontsize=8)
plt.subplot(323)
count, bins, ignored =plt.hist(r_walk, 20, normed=True, label='R_walk')
plt.legend(loc=0, fontsize=8)
plt.subplot(324)
count, bins, ignored =plt.hist(c_walk, 20, normed=True, label = 'C_walk')
plt.legend(loc=0, fontsize=8)
plt.subplot(325)
plt.scatter(r_walk, -np.log(l_walk), label='R_walk vs -log(l_walk)', color = 'green', s=8)
plt.legend(loc=0, fontsize=8)
plt.subplot(326)
plt.scatter(c_walk, -np.log(l_walk), label='C_walk vs -log(l_walk)', color='grey', s=8)
plt.legend(loc=0, fontsize=8)

plt.savefig('circuitoRC.png')




