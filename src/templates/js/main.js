const borrar =document.querySelectorAll('.btn_borar')

if(borrar){
    const btnArray=Array.from(borrar);
    btnArray.forEach((btn)=>{
        btn.addEventListener('click',(e)=>{
            if(!confirm('Estas seguro de eliminar el cliente')){
                e.preventDefault();
            }
        });
    });
}