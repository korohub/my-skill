<script>
	import { fade } from 'svelte/transition';
	import { fly } from 'svelte/transition';
	import { onMount } from 'svelte';
	import { Modals, closeModal, openModal, modals } from 'svelte-modals'
	import Modal from './Modal.svelte'
	
	
	let data = [];
	let filteredskill = [];
	let stringToMatch = '';
		
	onMount(async () => {
		const res = await fetch(`http://localhost:8000/skill`);
		data = await res.json();
		filteredskill = data;
	});

	function filterList(){
		filteredskill = data;
		if(stringToMatch){
			filteredskill = data.filter(data => {
				return data.Name.toLowerCase().includes(stringToMatch.toLowerCase()) 
			});
		}
	}

	function filtertech(param){		
		filteredskill = data;
		if(param){
			filteredskill = data.filter(data => {				
				return data.devops.toLowerCase().includes(param.toLowerCase()) 
			});		
		}
	}

	function handleOpen(term) {
		openModal(Modal, { 
			title: `Projet #${term}`,
			tech: term.toLowerCase(), 
			
			onOpenAnother: () => {
				handleOpen()
			}
		})
	}

	const ColorView = (color) => {
		switch (color) {
			case noob:
				color  = '"#ff6252;" class="stripes"';
				break;
			case middle:
				color  = '#54c6f9';
				break;
			case master:
				color  = '#2ecaac';
				break;
		}

	}
</script>

<div class="wrapper">
	<div class="header">
		<div class="description">
			<h2>My Skill</h2>			
			
			
		</div>

		<div class="ss">
		<img class="search-icon" src="data:image/svg+xml;utf8;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iaXNvLTg4NTktMSI/Pgo8IS0tIEdlbmVyYXRvcjogQWRvYmUgSWxsdXN0cmF0b3IgMTkuMC4wLCBTVkcgRXhwb3J0IFBsdWctSW4gLiBTVkcgVmVyc2lvbjogNi4wMCBCdWlsZCAwKSAgLS0+CjxzdmcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayIgdmVyc2lvbj0iMS4xIiBpZD0iQ2FwYV8xIiB4PSIwcHgiIHk9IjBweCIgdmlld0JveD0iMCAwIDU2Ljk2NiA1Ni45NjYiIHN0eWxlPSJlbmFibGUtYmFja2dyb3VuZDpuZXcgMCAwIDU2Ljk2NiA1Ni45NjY7IiB4bWw6c3BhY2U9InByZXNlcnZlIiB3aWR0aD0iMTZweCIgaGVpZ2h0PSIxNnB4Ij4KPHBhdGggZD0iTTU1LjE0Niw1MS44ODdMNDEuNTg4LDM3Ljc4NmMzLjQ4Ni00LjE0NCw1LjM5Ni05LjM1OCw1LjM5Ni0xNC43ODZjMC0xMi42ODItMTAuMzE4LTIzLTIzLTIzcy0yMywxMC4zMTgtMjMsMjMgIHMxMC4zMTgsMjMsMjMsMjNjNC43NjEsMCw5LjI5OC0xLjQzNiwxMy4xNzctNC4xNjJsMTMuNjYxLDE0LjIwOGMwLjU3MSwwLjU5MywxLjMzOSwwLjkyLDIuMTYyLDAuOTIgIGMwLjc3OSwwLDEuNTE4LTAuMjk3LDIuMDc5LTAuODM3QzU2LjI1NSw1NC45ODIsNTYuMjkzLDUzLjA4LDU1LjE0Niw1MS44ODd6IE0yMy45ODQsNmM5LjM3NCwwLDE3LDcuNjI2LDE3LDE3cy03LjYyNiwxNy0xNywxNyAgcy0xNy03LjYyNi0xNy0xN1MxNC42MSw2LDIzLjk4NCw2eiIgZmlsbD0iIzAwMDAwMCIvPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8L3N2Zz4K" alt="recherche" />
		<input placeholder="Recherche..." type="text" class="search" bind:value="{stringToMatch}" on:keyup="{filterList}">
		<img class="clear-icon" src="data:image/svg+xml;utf8;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iaXNvLTg4NTktMSI/Pgo8IS0tIEdlbmVyYXRvcjogQWRvYmUgSWxsdXN0cmF0b3IgMTkuMC4wLCBTVkcgRXhwb3J0IFBsdWctSW4gLiBTVkcgVmVyc2lvbjogNi4wMCBCdWlsZCAwKSAgLS0+CjxzdmcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayIgdmVyc2lvbj0iMS4xIiBpZD0iQ2FwYV8xIiB4PSIwcHgiIHk9IjBweCIgdmlld0JveD0iMCAwIDUxLjk3NiA1MS45NzYiIHN0eWxlPSJlbmFibGUtYmFja2dyb3VuZDpuZXcgMCAwIDUxLjk3NiA1MS45NzY7IiB4bWw6c3BhY2U9InByZXNlcnZlIiB3aWR0aD0iMTZweCIgaGVpZ2h0PSIxNnB4Ij4KPGc+Cgk8cGF0aCBkPSJNNDQuMzczLDcuNjAzYy0xMC4xMzctMTAuMTM3LTI2LjYzMi0xMC4xMzgtMzYuNzcsMGMtMTAuMTM4LDEwLjEzOC0xMC4xMzcsMjYuNjMyLDAsMzYuNzdzMjYuNjMyLDEwLjEzOCwzNi43NywwICAgQzU0LjUxLDM0LjIzNSw1NC41MSwxNy43NCw0NC4zNzMsNy42MDN6IE0zNi4yNDEsMzYuMjQxYy0wLjc4MSwwLjc4MS0yLjA0NywwLjc4MS0yLjgyOCwwbC03LjQyNS03LjQyNWwtNy43NzgsNy43NzggICBjLTAuNzgxLDAuNzgxLTIuMDQ3LDAuNzgxLTIuODI4LDBjLTAuNzgxLTAuNzgxLTAuNzgxLTIuMDQ3LDAtMi44MjhsNy43NzgtNy43NzhsLTcuNDI1LTcuNDI1Yy0wLjc4MS0wLjc4MS0wLjc4MS0yLjA0OCwwLTIuODI4ICAgYzAuNzgxLTAuNzgxLDIuMDQ3LTAuNzgxLDIuODI4LDBsNy40MjUsNy40MjVsNy4wNzEtNy4wNzFjMC43ODEtMC43ODEsMi4wNDctMC43ODEsMi44MjgsMGMwLjc4MSwwLjc4MSwwLjc4MSwyLjA0NywwLDIuODI4ICAgbC03LjA3MSw3LjA3MWw3LjQyNSw3LjQyNUMzNy4wMjIsMzQuMTk0LDM3LjAyMiwzNS40NiwzNi4yNDEsMzYuMjQxeiIgZmlsbD0iIzAwMDAwMCIvPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+CjxnPgo8L2c+Cjwvc3ZnPgo=" alt="recherche"/>
		</div>
		<div class="select">
			<button class="button dev" on:click="{() => filtertech("dev")}">DEV</button>
			<button class="button ops" on:click="{() => filtertech("ops")}">OPS</button>
			<button class="button reset" on:click="{() => filtertech("")}">Reset</button>		
		</div>



		
		
		<!-- <div class="auth">login</div> -->
	</div>
	<div class="skill">
		<div class="skill__row skill__row--months">
			<div class="skill__row-first"></div>
			<span>2000</span><span>2001</span><span>2002</span>
			<span>2003</span><span>2004</span><span>2005</span>
			<span>2006</span><span>2007</span><span>2008</span>
			<span>2009</span><span>2010</span><span>2011</span>
			<span>2012</span><span>2013</span><span>2014</span>
			<span>2015</span><span>2016</span><span>2017</span>
			<span>2018</span><span>2019</span><span>2020</span>
			<span>2021</span><span>2022</span><span>2023</span>
		</div>
		<div class="skill__row skill__row--lines" data-month="5">
			<span></span><span></span><span></span>
			<span></span><span></span><span></span>
			<span></span><span></span><span></span>
			<span></span><span></span><span></span>
			<span></span><span></span><span></span>
			<span></span><span></span><span></span>
			<span></span><span></span><span></span>
			<span ></span><span class="marker"></span><span></span>
		</div>

		{#each filteredskill as d }
		
			
			<div class="skill__row" transition:fade>
				<div class="skill__row-first">
					{d.Name}
					
				</div>
				<ul class="skill__row-bars" transition:fly="{{ x: 200, duration: 2000 }}">
				
					<li on:click={() => handleOpen(d.Slug)} style='grid-column: {parseInt(d.StartDate.toString().slice(-2))+2}/{parseInt(d.EndDate.toString().slice(-2))+2}; background-color: {d.Level}'>{d.EndDate- d.StartDate} {d.EndDate- d.StartDate === 1 ? 'an' : 'ans'} </li>
					
					
				</ul>
			</div>
		{:else}
				<!-- this block renders when photos.length === 0 -->
				<p>loading...</p>

		{/each}
	</div>
</div>

<Modals>
  <div
    slot="backdrop"
    class="backdrop"
		transition:fade
    on:click={closeModal}
  />
</Modals>

<style>	
	.backdrop {
    position: fixed;
    top: 0;
    bottom: 0;
    right: 0;
    left: 0;
    background: rgba(0,0,0,0.50)
  }

	.header {
	position: relative;
	color: #e0e1e6;
	margin-bottom: 20px;
	}
	/* .description{
	position: absolute;
	max-width: 80%;

	} */
	.header h2 {
	font-weight: 600;
	}
	.header p {
	font-weight: 300;
	}

	
	/* .auth {
	position: absolute;
	right: 50px;
	} */

	.wrapper {
	max-width: 1600px;
	min-width: 500px;
	margin: 0 auto;
	padding: 40px; 
	
	}
	

	.skill {
	display: grid;
	border: 0;
	border-radius: 10px;
	position: relative;
	overflow: hidden;
	box-sizing: border-box;
	box-shadow: 0 75px 125px -57px #7e8f94;
	}
	.skill__row {
	display: grid;
	grid-template-columns: 80px 1fr;
	background-color: #fff;
	}
	.skill__row:nth-child(odd) {
	background-color: #f5f5f5;
	}
	.skill__row:nth-child(odd) .skill__row-first {
	background-color: #f5f5f5;
	}
	.skill__row:nth-child(3) .skill__row-bars {
	border-top: 0;
	}
	.skill__row:nth-child(3) .skill__row-first {
	border-top: 0;
	}
	.skill__row--empty {
	background-color: #ffd6d2 !important;
	z-index: 1;
	}
	.skill__row--empty .skill__row-first {
	border-width: 1px 1px 0 0;
	}
	.skill__row--lines {
	position: absolute;
	height: 100%;
	width: 100%;
	background-color: transparent;
	grid-template-columns: 110px repeat(24, 1fr);
	}
	.skill__row--lines span {
	display: block;
	border-right: 1px solid rgba(0, 0, 0, 0.1);
	}
	.skill__row--lines span.marker {
	background-color: rgba(10, 52, 68, 0.13);
	z-index: 0;
	}
	.skill__row--lines:after {
	grid-row: 1;
	grid-column: 0;
	background-color: #1688b345;
	z-index: 2;
	height: 100%;
	}
	.skill__row--months {
	color: #fff;
	background-color: #0a3444 !important;
	border-bottom: 1px solid rgba(0, 0, 0, 0.9);
	grid-template-columns: 110px repeat(24, 1fr);
	}
	.skill__row--months .skill__row-first {
	border-top: 0 !important;
	background-color: #0a3444 !important;
	}
	.skill__row--months span {
	text-align: center;
	font-size: 13px;
	align-self: center;
	font-weight: bold;
	padding: 20px 0;
	}
	.skill__row-first {
	background-color: #fff;
	border-width: 1px 0 0 0;
	border-color: rgba(0, 0, 0, 0.1);
	border-style: solid;
	padding: 10px 0;
	font-size: 13px;
	font-weight: bold;
	text-align: center;
	}
	.skill__row-bars {
	list-style: none;
	display: grid;
	padding: 9px 0;
	margin: 0;
	grid-template-columns: repeat(24, 1fr);
	grid-gap: 8px 0;
	border-top: 1px solid rgba(221, 221, 221, 0.8);
	}
	.skill__row-bars li {
	font-weight: 500;
	/* text-align: left; */
	font-size: 14px;
	min-height: 15px;
	background-color: #55de84;
	padding: 5px 5px;
	color: #fff;
	overflow: hidden;
	position: relative;
	cursor: pointer;
	border-radius: 10px;
	text-align: center;
	}
	.skill__row-bars li.stripes {
	background-image: repeating-linear-gradient(45deg, transparent, transparent 5px, rgba(255, 255, 255, 0.1) 5px, rgba(255, 255, 255, 0.1) 12px);
	}
	.skill__row-bars li:before, .skill__row-bars li:after {
	content: "";
	height: 100%;
	top: 0;
	z-index: 4;
	position: absolute;
	background-color: rgba(0, 0, 0, 0.3);
	}
	.skill__row-bars li:before {
	left: 0;
	}
	.skill__row-bars li:after {
	right: 0;
	}

	.ss {
  position: relative;
  display: flex;
  min-width: 100px;
}

.search {
  border: 1px solid grey;
  border-radius: 5px;
  height: 25px;
  width: 100%;
  padding: 2px 23px 2px 30px;
  outline: 0;
  background-color: #f5f5f5;
}

.search-icon {
  position: absolute;
  top: 8px;
  left: 8px;
  width: 14px;
}

.clear-icon {
  position: absolute;
  top: 9px;
  right: 8px;
  width: 12px;
  cursor: pointer;
  visibility: hidden;
}

.search:hover, .search:focus {
  border: 1px solid #009688;
  background-color: white;
}

button {
  background-color: #4CAF50; /* Green */
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
  border-radius: 5px;
}

.ops {background-color: #008CBA;}

.reset {background-color: #f44336;}

	
</style>