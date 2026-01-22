from experiment import run_experiment

def main():
    test_key = "Example_Public_Key_Only"
    final_state, (x, y, z), magic = run_experiment(test_key)

    print("Key:", test_key)
    print("Final state:", final_state)
    print("Bloch coords:", x, y, z)
    print("Magic number:", magic)

if __name__ == "__main__":
    main()
