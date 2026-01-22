from experiment import run_experiment

def main():
    key = "Example_Public_Key_Only"
    state, (x, y, z), magic = run_experiment(key)

    print("Key:", key)
    print("Final state:", state)
    print("Bloch coords:", x, y, z)
    print("Magic number:", magic)

if __name__ == "__main__":
    main()
