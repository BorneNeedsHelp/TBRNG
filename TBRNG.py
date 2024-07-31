import time
class TBRNG:
    @staticmethod
    def TBRNG():
        current_time = int(time.time())

        random_number = (current_time * 123456789) % 1000000
        random_decimal = float(random_number) / 10000

        return random_decimal

    @staticmethod
    def TBRNG_Int_Range(min_value, max_value):
        min_value = int(min_value)
        max_value = int(max_value)

        current_time = int(time.time())

        random_number = (current_time * 123456789) % (max_value - min_value + 1)
        scaled_number = min_value + random_number

        return scaled_number

    @staticmethod
    def TBRNG_Int():
        current_time = int(time.time())

        random_number = (current_time * 123456789) % 1000000
        return random_number

    @staticmethod
    def TBRNG_Range(min_value, max_value):
        min_value = int(min_value)
        max_value = int(max_value)

        current_time = int(time.time())

        random_number = (current_time * 123456789) % (max_value - min_value + 1)
        scaled_number = min_value + random_number + random_number

        return scaled_number / 10 % 1000

    @staticmethod
    def TBRNG_Binary():
        current_time = int(time.time())

        random_number = (current_time * 123456789) % 1000000

        return format(random_number, 'b')

    @staticmethod
    def TBRNG_Double():
        current_time = int(time.time())

        random_number = (current_time * 123456789) % 1000000
        random_decimal = float(random_number) / 10000

        return random_decimal / 10

    @staticmethod
    def TBRNG_Gauss():
        current_time = int(time.time())

        real = current_time * 123456789 % 100
        fake = real * 123456789 % 100

        gauss = complex(real, fake)

        return gauss

    @staticmethod
    def TBRNG_Average(times_to_recurculate):
        current_time = int(time.time())
        times = 0
        random_full = 0

        for i in range(1, int(times_to_recurculate)):
            random_number = (current_time * 123456789) % 1000000
            random_number += random_full
            times += 1
            time.sleep(1)

        return int(random_number // times)

    @staticmethod
    def TBRNG_Statistics(times_to_recurculate):
        current_time = int(time.time())
        random_full = 0

        for i in range(1, times_to_recurculate):
            random_number = (current_time * 123456789) % 1000000
            random_number += random_full
            time.sleep(1)

        return random_number

    @staticmethod
    def TBRNG_Sort(times_to_recalculate):
        current_time = int(time.time())
        lists = []

        for i in range(0, times_to_recalculate):
            random_number = (current_time * 123456789) % 1000000
            current_time = time.time()
            lists.append(random_number)
            time.sleep(0.15)

        for i2 in range(1, len(lists)):
            swapped = False

            for i3 in range(0, len(lists) - i2):

                if lists[i3] > lists[i3 + 1]:
                    lists[i3], lists[i3 + 1] = lists[i3 + 1], lists[i3]
                    swapped = True

            if not swapped:
                break

        return lists




#Borne_M_S 6/29/24 - 6/31/24. Please do not copy!
