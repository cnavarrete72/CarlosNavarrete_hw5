import numpy as np
import matplotlib.pyplot as plt
#Se importan los datos originales y se guardan en arreglos.
datos1=np.genfromtxt('Canal_ionico.txt')

x1=datos1[:,0]
y1=datos1[:,1]

#Se importan los datos de las caminatas y se guardan en arreglos.
walk1=np.genfromtxt('walk1.txt')

x_walk1=walk1[:,0]
y_walk1=walk1[:,1]
r_walk1=walk1[:,2]

#Se obtiene el radio maximo con su respectivo centro.
arg1=np.argmax(r_walk1)
x_opt1=x_walk1[arg1]
y_opt1=y_walk1[arg1]
r_opt1=r_walk1[arg1]

#Se generan las graficas.
plt.figure()
plt.subplot(221)
plt.scatter(x1, y1, s = 10, label='Moleculas')
plt.scatter(x_opt1, y_opt1, color='green', label='Centro', s=10)
ang = np.linspace(0, 2*np.pi, 100)
circ_x = (r_opt1-0.5)*np.cos(ang) +x_opt1
circ_y = (r_opt1-0.5)*np.sin(ang) +y_opt1
plt.plot(circ_x, circ_y, color='red', label='r_max')
plt.legend(loc=0, fontsize=8)
plt.title('$x=%f$, $y=%f$, $r=%f$' %(x_opt1, y_opt1, r_opt1), fontsize=9)
plt.subplot(222)
plt.scatter(x_walk1, y_walk1, label='x_walk vs y_walk', s=10)
plt.legend(loc=0, fontsize=8)
plt.subplot(223)
count, bins, ignored =plt.hist(x_walk1, 20, normed=True, label='x_walk')
plt.legend(loc=0, fontsize=8)
plt.subplot(224)
count, bins, ignored =plt.hist(y_walk1, 20, normed=True, label = 'y_walk')
plt.legend(loc=0, fontsize=8)

plt.savefig('walk1.png')

#El proceso es exactamente el mismo con el segundo grupo de datos.
datos2=np.genfromtxt('Canal_ionico1.txt')

x2=datos2[:,0]
y2=datos2[:,1]

walk2=np.genfromtxt('walk2.txt')

x_walk2=walk2[:,0]
y_walk2=walk2[:,1]
r_walk2=walk2[:,2]


arg2=np.argmax(r_walk2)
x_opt2=x_walk2[arg2]
y_opt2=y_walk2[arg2]
r_opt2=r_walk2[arg2]

plt.figure()
plt.subplot(221)
plt.scatter(x2, y2, s = 10, label='Moleculas')
plt.scatter(x_opt2, y_opt2, color='green', label='Centro', s=10)
ang2= np.linspace(0, 2*np.pi, 100)
circ_x2= (r_opt2-0.5)*np.cos(ang2) +x_opt2
circ_y2= (r_opt2-0.5)*np.sin(ang2) +y_opt2
plt.plot(circ_x2, circ_y2, color='red', label='r_max')
plt.legend(loc=0, fontsize=8)
plt.title('$x=%f$, $y=%f$, $r=%f$' %(x_opt2, y_opt2, r_opt2), fontsize=9)
plt.subplot(222)
plt.scatter(x_walk2, y_walk2, label='x_walk vs y_walk', s=10)
plt.legend(loc=0, fontsize=8)
plt.subplot(223)
count, bins, ignored =plt.hist(x_walk2, 20, normed=True, label='x_walk')
plt.legend(loc=0, fontsize=8)
plt.subplot(224)
count, bins, ignored =plt.hist(y_walk2, 20, normed=True, label = 'y_walk')
plt.legend(loc=0, fontsize=8)

plt.savefig('walk2.png')

