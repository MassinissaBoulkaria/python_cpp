CPPFLAGS=-I /usr/include/python3.6m
LIBS=-lpython3.6m -lboost_python3-py36

COMPOSANT = sha3

LIBSO = ${COMPOSANT}.so
LIBSO_OBJS = ${COMPOSANT}.o

include ../gcc.mk


all: $(LIBSO)
clean:
        rm -f ${LIBSO}  ${LIBSO_OBJS}


${DESTINATION_LIBSO}: ${LIBSO}
        cp $< $@
