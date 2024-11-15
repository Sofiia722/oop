class PhoneCall:
    def __init__(self, last_name, city_call, intercity_call, international_call):
        self.last_name = last_name
        self.city_call = city_call
        self.intercity_call = intercity_call
        self.international_call = international_call

 
    def calculate_total_with_tax(self):
        return (self.city_call + self.intercity_call + self.international_call) * 1.2

    # ����� ��� ����������� ���������� ��� �����
    def display_record(self):
        print(f"| {self.last_name:<15} | {self.city_call:10.2f} | {self.intercity_call:10.2f} | "
              f"{self.international_call:10.2f} | {self.calculate_total_with_tax():10.2f} |")


def main():
    # �������� ������� ������
    count = int(input("Enter the number of records: "))

    # ����� ��� ���������� ������
    records = []

    # �������� ����� ��� ������� ������
    for i in range(count):
        print(f"Record {i + 1}:")
        last_name = input("Last Name: ")
        city_call = float(input("Amount for city calls: "))
        intercity_call = float(input("Amount for intercity calls: "))
        international_call = float(input("Amount for international calls: "))

        # ��������� ��'���� PhoneCall
        records.append(PhoneCall(last_name, city_call, intercity_call, international_call))

    # ��������� ��������� �������
    print("| {0:<15} | {1:10} | {2:10} | {3:10} | {4:10} |".format(
        "Last Name", "City", "Intercity", "International", "Total with Tax"))
    print("-" * 70)

    # ��������� ����� ��� ������� ������
    for record in records:
        record.display_record()

    # ���������� ��������� ���
    total_city = sum(record.city_call for record in records)
    total_intercity = sum(record.intercity_call for record in records)
    total_international = sum(record.international_call for record in records)
    total_with_tax = sum(record.calculate_total_with_tax() for record in records)

    # ��������� ��������� ���
    print("-" * 70)
    print(f"| {'Total':<15} | {total_city:10.2f} | {total_intercity:10.2f} | "
          f"{total_international:10.2f} | {total_with_tax:10.2f} |")


# ������ ������� ��������
if __name__ == "__main__":
    main()

