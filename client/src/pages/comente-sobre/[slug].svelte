<script>
  import { params } from '@roxi/routify'

  const slug = $params.slug

  async function getComments() {
    const res = await fetch(
      `https://comente-sobre-api.herokuapp.com/api/comments?thread=${slug}`)
    return await res.json()
  }

  async function getThread() {
    const res = await fetch(
      `https://comente-sobre-api.herokuapp.com/api/threads?slug=${slug}`)
    return await res.json()
  }

  async function createComment(thread, author_email, content) {
		const data = { thread: thread, author_email : author_email, content: content}
		const res = await fetch(
            'https://comente-sobre-api.herokuapp.com/api/comments/', {
			method: 'POST',
			headers: {
      			'Content-Type': 'application/json'
			},
			body: JSON.stringify(data)
		})

        return res.json()
  }

  function appendComment(author_email, content) {
    const comments_list = document.querySelector('#comments-list')

    const comment_li_str = (`
    <li>
      <h4>🗣️ ${author_email}</h4>
      <p>${content}</p>
    </li>`)

    comments_list.insertAdjacentHTML('afterbegin', comment_li_str)
    console.log(comments_list.innerHMTL)
  }

  function handleCommentComposer(e) {
    e.preventDefault()
	const formData = new FormData(e.target)
    const thread = formData.get('thread')
    const author_email = formData.get(`author_email`)
    const content = formData.get(`content`)
	createComment(thread,author_email,content)
    .then(() => { appendComment(author_email, content) } )
    e.target.reset()
  }
</script>
{#await getThread()}
    ...waiting
{:then thread}
    <h1>{thread[0].title}</h1>
    <div id="comment-composer">
        <form on:submit={handleCommentComposer}>
            <h2>Novo comentário</h2>
            <input type="email" name="author_email" id="email" placeholder="Insira seu email"/>
            <input type="hidden" name="thread" value={thread[0].id}/>
            <textarea name="content" placeholder="O que acha?"></textarea>
            <button>Enviar</button>
        </form>
    </div>
{:catch error}
<p style="color: red">{error.message}</p>
{/await}
<section class="comment">
{#await getComments()}
    <p>...waiting</p>
{:then comments}
    <h2>Comentários</h2>
    <ul id="comments-list">
        {#each comments as comment}
            <li>
              <h4>🗣️ {comment.author_email}</h4>
              <p>{comment.content}</p>
            </li>
        {/each}
    </ul>
    {:catch error}
    <p style="color: red">{error.message}</p>
    {/await}
</section>
