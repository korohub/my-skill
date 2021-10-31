<script>
    import { onMount } from 'svelte';
    import { closeModal, closeAllModals, openModal, modals } from 'svelte-modals'
    import { fly } from 'svelte/transition'
    

    export let isOpen
    export let title
    export let tech;
    export let onOpenAnother
	
	let stackIndex = $modals.length

    let data = [];
    onMount(async () => {
		const res = await fetch(`http://localhost:8000/details/${tech}`);
		data = await res.json();
		
	});

    
</script>

{#if isOpen}
	<!-- on:introstart and on:outroend are required to transition 1 at a time between modals -->
  <div role="dialog" class="modal" transition:fly={{ y: 50 }} on:introstart on:outroend>
    <div class="contents">
    {#if data != ''}
        <h1>Projet(s) avec {tech}</h1>
        {#each data as d }        
        <p>{@html d.Description}</p>
        <br>
        {/each}
    {:else}
        <p>Pas encore de projet Saisie</p>
    {/if} 
      <div class="actions">
				
			<button on:click={closeModal}>Close</button>							
        				
      </div>
    </div>
  </div>
{/if}

<style>
  .modal {
    height: 100vh;  
    position: fixed;
    top: 0;
    bottom: 120px;
    right: 50px;
    left: 50px;
    display: flex;
    justify-content: center;
    align-items: center;
    overflow-y:auto;
    

    /* allow click-through to backdrop */
    pointer-events: none;
  }

  .contents {
    min-width: 240px;
    border-radius: 6px;
    padding: 16px;
    background: white;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    pointer-events: auto;
    
  }

  h1 {
    text-align: center;
    font-size: 24px;
  }

  p {
    text-align: left;
    margin-top: 16px;
  }

  .actions {
    margin-top: 32px;
    display: flex;
    justify-content: flex-end;
		gap: 8px;
  }

</style>