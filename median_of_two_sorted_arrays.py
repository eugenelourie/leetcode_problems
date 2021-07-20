from typing import List


class Solution:
	def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
		n1, n2 = len(nums1), len(nums2)
		odd = (n1 + n2) % 2
        
		if odd:
			return float(self.get_kth(nums1, nums2, (n1 + n2) // 2))
		return (self.get_kth(nums1, nums2, (n1 + n2) // 2 - 1) + 
				self.get_kth(nums1, nums2, (n1 + n2) // 2)) / 2


	def get_kth(self, a, b, k):  # k in {0, ..., len(a) + len(b) - 1}
		i, j = -1, -1  # initial values are -1 as we haven't include any elements yet
		na, nb = len(a), len(b)

		# We are trying to find such i, j that i+j+1 corresponds to the index of median in sorted merged array
		while i + j + 1 < k:
			# We will do steps of length equal to the half of remaining distance 
			# between median index and sum of our indices
			step = (k - i - j) // 2
            
			# if our step brings us out of bounds, than we're sure we should do this step in other array
			if i + step >= na:
				j += step
				continue
			if j + step >= nb:
				i += step
				continue

			# Otherwise we choose the array with lesser element after the step
			if a[i + step] < b[j + step]:
				i += step
			else:
				j += step

		if i == -1:
			return b[j]
		if j == -1:
			return a[i]
		return max(a[i], b[j])
