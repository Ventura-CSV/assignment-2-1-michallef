def main():
    males = (int(input("Enter the number of males in the class: ")))
    females = (int(input("Enter the number of females in the class: ")))
    total = (males + females)
    m_perc = males / total * 100
    f_perc = females / total * 100
    print (f'The total number of students:   \t    {total}')
    print (f'The number of males and females: \t    {males} \t         {females}')
    print (f'The percentage of males and females: \t    {m_perc:.2f}% \t {f_perc:.2f}%')
    

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()
