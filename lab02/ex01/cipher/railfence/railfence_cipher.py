class RailFenceCipher:

    def rail_fence_encrypt(self, plain_text, num_rails):
        if num_rails <= 1 or num_rails >= len(plain_text):
            return plain_text

        rails = [[] for _ in range(num_rails)]

        rail_index = 0
        direction = 1

        for char in plain_text:
            rails[rail_index].append(char)

            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1

            rail_index += direction

        cipher_text = ''.join(''.join(rail) for rail in rails)

        return cipher_text

    def rail_fence_decrypt(self, cipher_text, num_rails):
        if num_rails <= 1 or num_rails >= len(cipher_text):
            return cipher_text

        text_length = len(cipher_text)

        pattern = [[False for _ in range(text_length)]
                   for _ in range(num_rails)]

        row = 0
        direction = 1

        for col in range(text_length):
            pattern[row][col] = True

            if row == 0:
                direction = 1
            elif row == num_rails - 1:
                direction = -1

            row += direction

        index = 0

        for r in range(num_rails):
            for c in range(text_length):
                if pattern[r][c]:
                    pattern[r][c] = cipher_text[index]
                    index += 1

        plain_text = ""

        row = 0
        direction = 1

        for col in range(text_length):
            plain_text += pattern[row][col]

            if row == 0:
                direction = 1
            elif row == num_rails - 1:
                direction = -1

            row += direction

        return plain_text