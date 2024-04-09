# Ćwiczenie 1
1)
a) rodzeństwo,
b) kuzyn,
c) wspołdziadkowie,
d) macocha
e) przyrodnie rodzenstwo
f) szwagier
g) wujek i przyrodnie rodzenstwo

2)
f(jan, anna).
f(jan, marek).
f(maria, anna).
f(maria, marek).
f(anna, kasia).
f(anna, tomasz).
f(tomasz, krzysztof).

mezczyzna(jan).
mezczyzna(marek).
mezczyzna(tomasz).
mezczyzna(krzysztof).

kobieta(anna).
kobieta(maria).
kobieta(kasia).

jest_małżonkiem(jan, maria).

jest_rodzenstwem(X, Y) :-
    f(Z, X),
    f(Z, Y),
    X \= Y.

jest_kuzynem(X, Y) :-
    f(A, X),
    f(B, Y),
    jest_rodzenstwem(A, B),
    A \= B,
    X \= Y.

są_wspólnymi_dziadkami(X, Y) :-
    f(A, X),
    f(A, Y),
    f(B, A),
    f(C, A),
    B \= C.

jest_macocha(X, Y) :-
    f(Z, Y),
    kobieta(X),
    \+ f(X, Y),
    f(Z, _).

jest_przyrodnim_rodzenstwem(X, Y) :-
    f(A, X),
    f(B, Y),
    \+ jest_rodzenstwem(A, B),
    A \= B,
    X \= Y.

jest_szwagrem(X, Y) :-
    jest_małżonkiem(X, Z),
    jest_rodzenstwem(Z, Y),
    mezczyzna(X). 

jest_wujkiem(X, Y) :-
    f(Z, Y),
    f(Z, X),
    mezczyzna(X),
    X \= Y.

jest_przyrodnim_rodzenstwem_wujka(X, Y) :-
    f(Z, X),
    jest_przyrodnim_rodzenstwem(Z, Y).

