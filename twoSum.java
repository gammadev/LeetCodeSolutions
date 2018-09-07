class Solution {
    Map<Integer, Integer> map = new HashMap<Integer, Integer>();
    public int[] twoSum(int[] nums, int target) {
        for (int i = 0; i < nums.length; ++i) {
            int complement = target - nums[i];
            if (map.containsKey(complement)) {
                int index = map.get(complement);
                int[] ans = {i, index};
                return ans;
            }
            map.put(nums[i], i);
        }
        return null;
    }
}
