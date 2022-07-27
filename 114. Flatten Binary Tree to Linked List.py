 class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        
        def rightmost(root):
            if (root.right):
                return rightmost(root.right)
            return root
        
        if root:
            nextright = None
            rightone = None
        
        while root:
            if root.left:
                rightone = rightmost(root.left);
                nextright = root.right;
                root.right = root.left;
                root.left = None;
                rightone.right = nextright;
            root=root.right
            
            
  #RESULT: 29ms
