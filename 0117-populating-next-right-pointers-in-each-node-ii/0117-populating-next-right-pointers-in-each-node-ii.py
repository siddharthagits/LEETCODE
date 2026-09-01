class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        q = root
        
        while q:
            head = None
            prev = None
            k = q
            
            while k:
                if k.left:
                    if not head:
                        head = k.left
                    if prev:
                        prev.next = k.left
                    prev = k.left
                
                if k.right:
                    if not head:
                        head = k.right
                    if prev:
                        prev.next = k.right
                    prev = k.right
                
                k = k.next
            
            q = head
        
        return root