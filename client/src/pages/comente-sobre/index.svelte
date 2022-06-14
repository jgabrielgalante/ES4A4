<script>
	import { goto } from '@roxi/routify'

	function creteThread(title){
		const data = { title: title}

		fetch('https://comente-sobre-api.herokuapp.com/api/threads/', {
			method: 'POST',
			headers: {
      			'Content-Type': 'application/json'
			},
			body: JSON.stringify(data)
		})
		.then(r => { return r.json() })
		.then(j => { $goto(`./${j.slug}`) })
	}

	function handleForm(e) {
		e.preventDefault()
		const formData = new FormData(e.target)
		creteThread(formData.get('title'))
	}

</script>
<div class="search-box">
    <div class="input-group">
        <form on:submit={handleForm}>
            <input id="tema" name="title" type="text" placeholder="Pesquise um assunto">
            <button>
                🔎
            </button>
        </form>
    </div>
</div>
