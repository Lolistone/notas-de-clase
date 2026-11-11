import random
 
 
def polya_urn(steps: int) -> float:
    """Simula la urna de Pólya por steps extracciones.
    Comienza con 1 bola roja y 1 verde.
    Devuelve la fracción de bolas rojas al final.
    """
    red, green = 1, 1
    for _ in range(steps):
        total = red + green
        if random.random() < red / total:
            red += 1
        else:
            green += 1
    return red / (red + green)
 
 
def run_simulation(n_runs: int = 20, steps_1: int = 600, steps_2: int = 1200) -> None:

    print(f"{'Ejecución':>10} | {'n='+str(steps_1):>8} | {'n='+str(steps_2):>8} | {'Diferencia':>10}")
    print("-" * 46)
 
    fracs_1, fracs_2 = [], []
 
    for i in range(1, n_runs + 1):
        f1  = polya_urn(steps_1)
        f2 = polya_urn(steps_2)
        fracs_1.append(f1)
        fracs_2.append(f2)
        print(f"{i:>10} | {f1:>8.4f} | {f2:>8.4f} | {abs(f1 - f2):>10.4f}")
 
    print("-" * 46)
    print(f"{'Media':>10} | {sum(fracs_1)/n_runs:>8.4f} | {sum(fracs_2)/n_runs:>8.4f}")
    print()
 
 
if __name__ == "__main__":
    run_simulation(n_runs=100, steps_1=600, steps_2=1200)
