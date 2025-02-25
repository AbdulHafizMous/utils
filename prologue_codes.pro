/*
pere(stanislas, jean).
 stanislas est le pere de jean 
pere(edmond, eve).
pere(jean, anne).
pere(jean, ange).
mere(cecile, jean). 
mere(jeanne, eve).
mere(eve, anne).
mere(eve, ange).
grandpere(A, B) :- pere(A,X) , pere(X,B).
grandpere(A, B) :- pere(A,X) , mere(X,B).


concat2([], [], []).
concat2([T|_], [], [T|_]).
concat2([T|Q], [], [T|Q]).
concat2([], [T|_], [T|_]).
concat2([], [T|Q], [T|Q]).
concat2([T|Q], [L|_], [L|[T|Q]]).
concat2([T|Q], [L|M], Rf) :- concat2([T|Q], [L|_], Tf), concat2(Tf, M, Zf), Rf is Zf.
*/







fact(0, 1).
fact(N, Nf) :- N > 0, M is N-1, fact(M, Mf), Nf is N*Mf.
%fact(N, Nf) :- N > 0, fact(N-1, Mf), Nf is N*Mf.

appart(X, [T|Q]) :- X is T.
appart(X, [_|Q]) :- appart(X, Q).

long([], 0).
long([_|Q], Lf) :- long(Q, N1), Lf is 1+N1.

somo(1, 1).
somo(N, Nf) :- N > 1, M is N-1, somo(M, Mf), Nf is N+Mf.

hors_de(X, []).
hors_de(X, [T|Q]) :- X \= T, hors_de(X,Q).

concat([], L, L).
concat([T|Q], L, [T|R]) :- concat(Q,L,R).

enlever(X, [], []).
enlever(X, [T|Q], Q) :- X = T.
enlever(X, [T|Q], [T|R]) :- X \= T, enlever(X, Q, R).

reverse([], []).
reverse([T|Q], R) :- reverse(Q, Qo), concat(Qo, [T], R).

sorto([], []).
sorto([T|[]], [T|[]]).
sorto([T|Q], R) :- sorto(Q, [To|Qo]), T > To, concat([T], [To|Qo], R).
sorto([T|Q], R) :- sorto(Q, [To|Qo]), T < To, sorto([T|Qo], C), concat([To], C, R).











