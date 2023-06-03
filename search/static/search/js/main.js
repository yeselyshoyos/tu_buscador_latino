baseUrl = window.location.origin;
var App = Vue.createApp({
    delimiters: ['[[', ']]'],
    data() {
        return {
            consult: "",
            word: "",
        }
    },
    methods: {
      save_searches(){
        let bodyFormData = new FormData()
        bodyFormData.append('consult', this.consult)
        bodyFormData.append('number_of_results', 1)
        axios.post(baseUrl + "/save_searches", bodyFormData)
        .then(function (response) {
          console.log(response)
          app.consult = "";
        })
        .catch(function (error) {
          console.log(error);
        });
      },
    }
});
var app = App.mount('#app')