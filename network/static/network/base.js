var csrftoken = Cookies.get('csrftoken');
function edit(id){
  var editbox=document.querySelector(`#edit-box-${id}`);
  var editbtn=document.querySelector(`#edit-btn-${id}`);
  editbox.style.display='block';
  editbtn.style.display='block';
 editbox.value=document.querySelector(`#post-${id}`).innerHTML

  editbtn.addEventListener('click',() => {
       fetch('/edit/' +id, {
            method: 'PUT',

            headers: { "X-CSRFToken": csrftoken },
            body: JSON.stringify({
            pos: editbox.value
            })
       });

  editbox.style.display='none'
  editbtn.style.display='none';

  document.querySelector(`#post-${id}`).innerHTML=editbox.value;
  });

}
function like(id){
  var lbtn=document.querySelector(`#like-btn-${id}`);
  var lct=document.querySelector(`#like-count-${id}`);

  lbtn.addEventListener('click',()=>{

      if(lbtn.style.backgroundColor == 'white'){
         fetch('/like/'+ id,{

          headers: { "X-CSRFToken": csrftoken },
          method:'PUT',
           body: JSON.stringify({
                    like: true
                })
          })
          lbtn.style.backgroundColor='red';


          fetch('/like/'+`${id}`)
          .then(res => res.json())
          .then(post=>{
              lct.innerHTML=post.likes;
          });
         }

      else{
        fetch('/like/' + id,{
           headers: { "X-CSRFToken": csrftoken },
           method:'PUT',
           body: JSON.stringify({
             like:false

         })

        });
           lbtn.style.backgroundColor = 'white';

            fetch('/like/'+`${id}`)
            .then(response => response.json())
            .then(post => {
                lct.innerHTML = post.likes;
            });
      }
      return false;
  });

}