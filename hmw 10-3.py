def get_statistics(nums: list[int]) -> dict:
    return {
        'max': max(nums),
        'min': min(nums),
        'sum': sum(nums),
        'len': len(nums),
        'avg': sum(nums)/len(nums),
    }


print(get_statistics(nums=[45, 5, 9, 64, 8, 4]))
