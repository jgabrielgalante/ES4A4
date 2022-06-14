<script>
  import { url } from '@roxi/routify'
</script>
<div class="wrapper">
	<header>
		<nav>
			<ul>
				<a href={$url('/comente-sobre')}>🏠 Início</a>
			</ul>
		</nav>
	</header>
	<main>
		<slot>
		</slot>
	</main>
</div>
