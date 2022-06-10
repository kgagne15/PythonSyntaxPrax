def in_range(nums, lowest, highest):
    """Print numbers inside range.

    - nums: list of numbers
    - lowest: lowest number to print
    - highest: highest number to print

    For example:

      in_range([10, 20, 30, 40], 15, 30)

    should print:

      20 fits
      30 fits
    """

    # YOUR CODE HERE
    num_range = []
    
    for num in nums:
      if num >= lowest and num <= highest:
        num_range.append(num)
    lowest_in_range = num_range[0]
    highest_in_range = num_range[0]
    for num in num_range:
      if num < lowest_in_range:
        lowest_in_range = num
      if num > highest_in_range:
        highest_in_range = num

    
      
    print(lowest_in_range, ' fits')
    print(highest_in_range, ' fits')


in_range([10, 20, 30, 40, 50], 15, 30) 
# in_range([100, 5, 25, 1000, 3000], 20, 1000)  
        
