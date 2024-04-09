# Ćwiczenie 2
% Fakty
osoba(jan).
osoba(anna).
osoba(maria).
osoba(piotr).
osoba(krzysztof).

mezczyzna(jan).
mezczyzna(piotr).
mezczyzna(krzysztof).

kobieta(anna).
kobieta(maria).

rodzic(jan, anna).
rodzic(jan, piotr).
rodzic(anna, maria).
rodzic(piotr, krzysztof).

:- discontiguous kobieta/1.
kobieta(X) :- 
    osoba(X),
    \+mezczyzna(X).

ojciec(X, Y) :- 
    mezczyzna(X), 
    rodzic(X, Y).

matka(X, Y) :- 
    kobieta(X),
    rodzic(X, Y).

corka(X, Y) :- 
    kobieta(X),
    rodzic(Y, X).

brat_rodzony(X, Y) :- 
    mezczyzna(X), 
    rodzic(Z, X),
    rodzic(Z, Y),
    X \= Y.

brat_przyrodni(X, Y) :-
    mezczyzna(X),
    rodzic(Z, X),
    rodzic(W, Y),
    \+rodzic(Z, Y),
    \+rodzic(W, X),
    X \= Y.

kuzyn(X, Y) :- 
    rodzic(Z, X),
    rodzic(W, Y),
    (brat_rodzony(Z, W); 
    brat_przyrodni(Z, W)).

dziadek_od_strony_ojca(X, Y) :-
    mezczyzna(X), 
    rodzic(X, Z),
    rodzic(Z, Y).

dziadek_od_strony_matki(X, Y) :- 
    mezczyzna(X),
    matka(Z, Y),
    rodzic(X, Z).

dziadek(X, Y) :- 
    dziadek_od_strony_ojca(X, Y); 
    dziadek_od_strony_matki(X, Y).

babcia(X, Y) :-
    kobieta(X),
    matka(X, Z),
    rodzic(Z, Y).

wnuczka(X, Y) :- 
    babcia(X, Y),
    kobieta(Y).

przodek_do2pokolenia_wstecz(X, Y) :-
    rodzic(X, Z),
    rodzic(Z, Y).

przodek_do3pokolenia_wstecz(X, Y) :-
    rodzic(X, Z), 
    przodek_do2pokolenia_wstecz(Z, Y).

