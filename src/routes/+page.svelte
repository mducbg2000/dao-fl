<script lang="ts">
	import { Toast, toastStore } from '@skeletonlabs/skeleton';
	import type { ToastSettings } from '@skeletonlabs/skeleton';
	let name = '';

	function triggerAlert() {
		const t: ToastSettings = {
			message: `Hello ${name}`,
			timeout: 20000,
			background: 'variant-filled-success'
		};
		toastStore.trigger(t);
	}
</script>

<div class="p-8">
	<label class="label">
		<span>Your name:</span>
		<input class="input" type="text" placeholder="Input" bind:value={name} />
	</label>
	<button type="button" class="btn variant-filled-primary mt-4 ripple" on:click={triggerAlert}>
		Say hi
	</button>
	{#if name.length > 0}
		<h2>Your name is {name}?</h2>
	{/if}
	<Toast />
</div>
