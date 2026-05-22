class Solution:
    def maxArea(self, a: List[int]) -> int:
        # min(a[l], a[r]) * (r-l)
        n = len(a)
        if n ==2:
            return min(a[0], a[1])
        vmax=0
        for i  in range(n):
            l, r=i+1, n-1
            while l<r:
                ht_lr = min(a[l], a[r])
                width_lr = r-l
                v_lr = ht_lr*width_lr
                # print(f"v_lr: {v_lr}")

                ht_ir = min(a[i], a[r])
                width_ir = r-i
                v_ir = ht_ir*width_ir
                # print(f"v_ir: {v_ir}")

                ht_il = min(a[i], a[l])
                width_il = l-i
                v_il = ht_il*width_il
                # print(f"v_il: {v_il}")

                vmax = max(vmax, max(v_lr, max(v_ir, v_il)))
                
                while l<r and a[l] == a[l+1]:
                    l+=1
                while l<r and a[r-1] == a[r]:
                    r-=1
                l+=1
                r-=1
        return vmax
        
        