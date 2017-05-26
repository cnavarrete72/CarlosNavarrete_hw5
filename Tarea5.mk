Resultados_hw5.pdf : Resultados_hw5.tex walk1.png walk2.png circuitoRC.png
	pdflatex Resultados_hw5.tex

walk1.png walk2.png : plots_canal_ionico.py walk1.txt walk2.txt
	python plots_canal_ionico.py

walk1.txt walk2.txt : a.out Canal_ionico.txt Canal_ionico1.txt
	./a.out

a.out : canal_ionico.c
	cc canal_ionico.c -lm

circuitoRC.png : circuitoRC.py CircuitoRC.txt
	python $<
