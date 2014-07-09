nums = raw_input('enter numbers: ')
nums = nums.split(',')
nums = map(int, nums)

def run(nums, used, current):
	if all(used):
		return {
			'success': True,
			'steps': ()
		}
	used = list(used)
	if used[current]:
		return {
			'success': False,
			'steps': None
		}
	step = nums[current]
	used[current] = True

	result = run(nums, used, (current + step) % len(nums))
	if (result['success']):
		return {
			'success': True,
			'steps': (current,) + result['steps']
		}

	result = run(nums, used, (current - step + len(nums)) % len(nums))
	if (result['success']):
		return {
			'success': True,
			'steps': (current,) + result['steps']
		}

	return {
		'success': False,
		'steps': None
	}

for i, start in enumerate(nums):
	used = [False] * len(nums)
	result = run(nums, used, i)
	if result['success']:
		print result['steps']

