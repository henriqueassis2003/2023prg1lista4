def search_rotated(nums, target):
    """
    Retorna o índice do elemento alvo em uma lista ordenada rotacionada, ou -1 se o elemento não estiver presente.
    """
    n = len(nums)
    if n == 0:
        return -1
    # Encontra o índice do pivô usando busca binária modificada
    left, right = 0, n-1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    pivot = left
    # Realiza busca binária normal na parte relevante da lista
    left, right = 0, n-1
    while left <= right:
        mid = (left + right) // 2
        mid_pivot = (mid + pivot) % n
        if nums[mid_pivot] == target:
            return mid_pivot
        elif nums[mid_pivot] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
