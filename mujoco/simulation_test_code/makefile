# organizing code compilation



COMMON=-O2 -I../../include -L../../bin -mavx -pthread -Wl,-rpath,'$$ORIGIN'
LIBS = -lmujoco210 -lGL -lm -lglew ../../bin/libglfw.so.3
CC = gcc

ROOT = projectile

all:
	$(CC) $(COMMON) main.c $(LIBS) -o ../../bin/$(ROOT)

main.o:
	$(CC) $(COMMON) -c main.c

clean:
	@echo "Cleaning up..."
	rm *.o ../../bin/$(ROOT)
