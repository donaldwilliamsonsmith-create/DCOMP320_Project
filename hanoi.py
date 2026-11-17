def hanoi(n, source, destination, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    hanoi(n - 1, source, auxiliary, destination)
    print(f"Move disk {n} from {source} to {destination}")
    hanoi(n - 1, auxiliary, destination, source)

if __name__ == "__main__":
    n_disks = 3
    print(f"--- Tower of Hanoi Solution for {n_disks} disks ---")
    hanoi(n_disks, 'A', 'C', 'B')
def hanoi(n, source, destination, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    hanoi(n - 1, source, auxiliary, destination)
    print(f"Move disk {n} from {source} to {destination}")
    hanoi(n - 1, auxiliary, destination, source)

if __name__ == "__main__":
    n_disks = 3
    print(f"--- Tower of Hanoi Solution for {n_disks} disks ---")
    hanoi(n_disks, 'A', 'C', 'B') 