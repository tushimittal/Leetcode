class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []
        current = 1

        for _ in range(n):
            result.append(current)

            # Try to go deeper in lexicographical order
            if current * 10 <= n:
                current *= 10
            else:
                # If not possible to go deeper, increment current
                if current >= n:
                    current //= 10
                current += 1
                # Remove trailing zeroes to keep within the range
                while current % 10 == 0:
                    current //= 10

        return result
