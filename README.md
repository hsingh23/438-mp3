Harsh Singh – hsingh23
Ziqi Peng – peng20

MP3 – REPORT

Part 1:
    If you run: python encoder.py -g # -k # -d # 
    -g is any generator int,
    -k is number of bits in the data input
    -d specifies the decimal equivalent of the data input

    with -g # -k # -d # specified - you will get the computed crc code

    with only -g # specified - you will get the performance results of the table based approach and the non-table based approach where the tests are run with specified generator and random data 1000000 times

    Performance Analysis:
        python encoder.py -g 9
        Stats - 1000000 runs - random data
        CRC:  19.4423699379
        <timeit-src>:2: SyntaxWarning: import * only allowed at module level
        CRC Table:  3.49995803833
        0.1 Probability with 10000 Executions
        Error Detected: 0.6112
        Error Not Detected: 0.0629
        0.2 Probability with 10000 Executions
        Error Detected: 0.8004
        Error Not Detected: 0.1132
        0.3 Probability with 10000 Executions
        Error Detected: 0.8594
        Error Not Detected: 0.121

        Here we see that as the channel gets noisy more packets get lost. Infact with a 30% chance of error - we lose over 10% of the packets 


Part2:
    run: python checksum.py 2000 121 4 53 221 856 10005 9345
    results "checksum: 42930 0b1010011110110010"
    The first number is the decimal checksum and the second number is the binary checksum.
    You can specify more than 9 words
