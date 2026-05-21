class Solution:
    def threeSum(self, a: List[int]) -> List[List[int]]:
        # sort the arr
        a.sort()
        n = len(a)
        triplet = []

        # 25/26 Test cases
        # for i in range(n):
        #     # smallest number is positive, sum cannot be zero
        #     if a[i]>0:
        #         break
            
        #     # skip repitions
        #     if i>0 and a[i-1]==a[i]:
        #         continue

        #     for j in range(i+1, n):
        #         # skip repitions except the first j
        #         if j != i+1 and a[j-1]==a[j]:
        #             continue
        #         if (a[i]+a[j]>0):
        #             # need k, s.t. k<0 and k = -a[i]-a[j]
        #             # req k D.N.E
        #             break
    
        #         if (a[i]+a[j]<0):
        #             # need k, s.t. k>0 and k = -a[i]-a[j]
        #             for k in range(j+1, n):
        #                 if a[k] == -a[i]-a[j]:
        #                     triplet.append([a[i],a[j],a[k]])
        #                     break

        #         if (a[i]+a[j]==0):
        #             # need k, s.t. k==0
        #             if a[j]>0:
        #                 # req k D.N.E
        #                 break
        #             for k in range(j+1, n):
        #                 if a[k]==0:
        #                     triplet.append([a[i],a[j],a[k]])
        #                     break

        for i in range(0,n):
            # smallest number is positive, sum cannot be zero
            if a[i]>0:
                break
            # skip repitions
            if i>0 and a[i-1]==a[i]:
                continue

            l, r = i+1, n-1
            while(l<r):
                s = a[i]+ a[l] +a[r]
                if s>0:
                    r-=1
                elif s<0:
                    l+=1
                else:
                    triplet.append([a[i], a[l], a[r]])
                    while l<r and a[l] == a[l+1]:
                        l+=1
                    while l<r and a[r] == a[r-1]:
                        r-=1
                    l+=1
                    r-=1
    
        return triplet