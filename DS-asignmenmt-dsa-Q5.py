def hanoiTower(n, from_rod='A', to_rod='B', aux_rod='C'):
    if n == 0:
        return
    hanoiTower(n-1, from_rod, aux_rod, to_rod)
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
    hanoiTower(n-1, aux_rod, to_rod, from_rod)
    
    
n = int(input('Enter the disks:'))
hanoiTower(n)
