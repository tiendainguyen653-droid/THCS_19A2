def tim_so_le_lon_nhat(a, b, c):
    so_le = [x for x in (a, b, c) if x % 2 != 0]
    if not so_le:
        return -1
    return max(so_le)

# Test
print(tim_so_le_lon_nhat(2, 9, 4))
