class LOGICAL:
    def sum_n(self,n):
        sum=0
        for i in range(n+1):
            sum+=i
        print(sum)
    def fact_n(self,n):
        prod=1
        for i in range(1,n+1):
            prod*=i
        return prod
    def factors(self,n):
        for i in range(1,n+1):
            if n%i==0:
                print(i,end=" ")
    def count_factors(self,n):
        count=0
        for i in range(1,n+1):
            if n%i==0:
                count+=1
        return count
    def isprime_no(self,n,/):
        if self.count_factors(n)==2:
            print(f"{n} is prime")
        else:
            print(f"{n} is not a prime")
    def reverse_number(self,n):
        rev=0
        while n:
            rem=n%10
            rev=rev*10+rem
            n//=10
        return rev

    def palindrome(self,n):
        if self.reverse_number(n)==n:
            print(f"{n} is a palindrome")
        else:
            print(f"{n} is not a palindrome")
    def digits_sum(self,n):
        sum=0
        while n:
            rem=n%10
            sum=sum+rem
            n//=10
        print(sum)
    def digit_count(self,n):
        count=0
        while n>0:
            count+=1
            n//=10
        print(count)
    def armstrong_num(self,n):
        sum=0
        val=n
        l=len(str(n))
        while n:
            rem=n%10
            sum+=rem**l
            n//=10
        print(sum)
        if val==sum:
            print(f"{val} is an armstrong number")
        else:
            print(f"{val} is not an armstrong number")
    def strong_numb(self,n):
        sum=0
        temp=n
        while n:
            sum+=self.factorial(n%10)
            n//=10
        if sum==temp:
            print(f"{temp} is a strong number")
        else:
            print(f"{temp} is not a strong number")