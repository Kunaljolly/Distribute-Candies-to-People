class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> list[int]:
        # Initialize the array to store the candies distributed to each person
        distribution = [0] * num_people
        current_candy = 1  # The first candy to be distributed
        index = 0  # Start with the first person

        # Continue distributing candies until we run out
        while candies > 0:
            # Calculate the candies to give this round
            if candies >= current_candy:
                distribution[index] += current_candy
                candies -= current_candy
            else:
                # If not enough candies are left, give all remaining candies
                distribution[index] += candies
                candies = 0

            # Move to the next person
            current_candy += 1
            index = (index + 1) % num_people

        return distribution
